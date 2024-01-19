
class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = "norm"
    def get_data_config(self, data_name):
        self.data_name = data_name
        if data_name == 'LEVIR':
            self.root_dir = '/workspace/test/LEVIR-CD-256/'
        elif data_name == 'DSIFN':
            self.root_dir = '/workspace/test/DSIFN-CD-256/'
        elif data_name == 'WHU':
            self.root_dir = '/workspace/test/WHU-224/'
        elif data_name == 'GOOGLE':
            self.root_dir = '/workspace/test/GOOGLE/'
        elif data_name == 'quick_start':
            self.root_dir = '/workspace/test/visualization/dsifn-256/'
        else:
            raise TypeError('%s has not defined' % data_name)
        return self


if __name__ == '__main__':
    data = DataConfig().get_data_config(data_name='LEVIR')
    print(data.data_name)
    print(data.root_dir)
    print(data.label_transform)

