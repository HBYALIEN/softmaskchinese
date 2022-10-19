import os
import platform
class Config(object):
    """
    参数管理器
    """
    def __init__(self):
        self.device = 'cuda'
        self.inference_device = 'cuda'

        self.bert_path = '/home/WIN-UNI-DUE/smbohann/softmask/chinese_wwm_ext_pytorch'
        self.vocab_file = '/home/WIN-UNI-DUE/smbohann/softmask/chinese_wwm_ext_pytorch/vocab.txt'
        # 预训练的模型文件地址，去transformers hugface官网下载即可
        self.hidden_size = 50  # 隐层维度
        self.embedding_size = 768  # embedding维度
        self.lr = 0.0001
        self.epoch = 10
        self.batch_size = 15

        self.datapath = '/home/WIN-UNI-DUE/smbohann/softmask/data/SIGHAN15_train.csv'

        self.checkpoints = '/home/WIN-UNI-DUE/smbohann/softmask/checkpoints'

    @staticmethod
    def platform():
        """
        Returns:
            返回当前操作系统名称,'Linux'或'Windows'
        """
        return platform.system()