"""日志处理封装的函数，目的：是将log日志输出与配置文件相结合"""
import logging
from Config import configs
import os


def get_logger(
        name='root',
        file=None,
        logger_level='DEBUG',
        stream_level='DEBUG',
        file_level='DEBUG',
        log_mode='w',
        fmt='%(asctime)s--%(filename)s--line:%(lineno)d--%(levelname)s:%(message)s'):
    """
    :param name:代表收集器名称，如果不传入参数时使用默认级别（waning）
    :param file: 指定日志文件存放的路径及名称
    :param logger_level: 收集器的收集等级
    :param stream_level: 输出处理器收集等级
    :param file_level: 控制台输出处理器收集等级
    :param log_mode: log日志文件存储模式
    :param fmt: 指定日志输出的格式
    """
    # 创建一个收集器，name代表收集器名称，如果不传入参数时使用默认级别（waning）
    logger = logging.getLogger(name)
    # 设置收集器的收集等级，longer_level带代表等级
    logger.setLevel(logger_level)
    # 创建一个输出处理器，收集输出信息
    stream_handler = logging.StreamHandler()
    # 设置输出器的输出等级，并在控制台显示
    stream_handler.setLevel(stream_level)
    # 指定日志输出的格式
    fmt = logging.Formatter(fmt)
    # 将日志格式添加到输出器中
    stream_handler.setFormatter(fmt)
    # 把输出处理器添加到收集器中
    logger.addHandler(stream_handler)
    # 不指定log输出文件时，只输出到控制台
    if file:
        # 设置输出到log文件中的log日志级别设置，
        file_path = os.path.join(configs.LOG_PATH, file)
        file_handle = logging.FileHandler(file_path, mode=log_mode, encoding='utf8')
        file_handle.name = file_handle.baseFilename
        # 重新定义输出到log文件中的输出器的级别，因为没有必要记录过于详细的日志
        file_handle.setLevel(file_level)
        logger.addHandler(file_handle)
        file_handle.setFormatter(fmt)
    return logger


if __name__ == '__main__':
    get_logger().info("*********")
    get_logger().info("*********")
