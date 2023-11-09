

class BarplotSimple():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x = list(self.data['x'])
        y = list(self.data['y'])

        options = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                'type': 'shadow'
                }
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [
                {
                'data': y,
                'type': 'bar'
                }
            ]
        }

        return options
    

class BarplotGrouped():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x = list(self.data.astype(str)['x'].unique())
        ys = dict()
        groups = self.data['groups']
        groups = list(groups.unique())
        print(self.data)
        print(groups)
        for name, s in self.data.groupby('groups'):
            y = list(s['y'])
            ys[name] = y
    
        series_list = list()

        for name, y in ys.items():
            d = {
                'name': name,
                'type': 'bar',
                'barGap': '0',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': y
            }
            series_list.append(d)
        
        options = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                'type': 'shadow'
                }
            },
            'legend': {
                'data': groups
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value'
            },
            'series': series_list
        }

        return options
    

class BarplotStacked():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x = list(self.data.astype(str)['x'].unique())
        ys = dict()
        stacks = self.data['stacks']
        groups = list(stacks.unique())
        for name, s in self.data.groupby('stacks'):
            y = list(s['y'])
            ys[name] = y
    
        series_list = list()
        for name, y in ys.items():
            d = {
                'name': name,
                'type': 'bar',
                'barGap': '0',
                'stack': 'total',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': y
            }
            series_list.append(d)
        
        options = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                'type': 'shadow'
                }
            },
            'legend': {
                'data': groups
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value'
            },
            'series': series_list
        }

        return options
    

class BarplotGroupedStacked():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x = list(self.data.astype(str)['x'].unique())
        # ys = dict()
        stacks = self.data['stacks']
        groups = list(stacks.unique())
        print('abcdefg')
        # for name, group_name, s in self.data.groupby(['stacks', 'groups']):
        series_list = list()
        for name, s in self.data.groupby(['groups', 'stacks']):
            group_name = name[0]
            stack_name = name[1]
            print(name)
            print(s)
            # print(group_name)
            y = list(s['y'])
            # ys[name] = y

            d = {
                'name': stack_name,
                'type': 'bar',
                'barGap': '0',
                'stack': f'{group_name}',
                'label': {
                    'show': True
                },
                'emphasis': {
                    'focus': 'series'
                },
                'data': y
            }
            series_list.append(d)
    
        # series_list = list()
        # for name, y in ys.items():
        #     d = {
        #         'name': name,
        #         'type': 'bar',
        #         'barGap': '0',
        #         'stack': 'Ad',
        #         'label': {
        #             'show': True
        #         },
        #         'emphasis': {
        #             'focus': 'series'
        #         },
        #         'data': y
        #     }
        #     series_list.append(d)
        
        options = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                'type': 'shadow'
                }
            },
            'legend': {
                'data': groups
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value'
            },
            'series': series_list
        }

        return options





        