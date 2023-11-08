

class BarplotSimple():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def gen_options(self):
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

    def gen_options(self):
        x = list(self.data.astype(str)['x'].unique())
        ys = dict()
        groups = self.data['groups']
        groups = list(groups.unique())
        for name, s in self.data.groupby(groups):
            y = list(s['y'])
            ys[name] = y
    
        series_list = list()

        for name, y in ys.items():
            d = {
                'name': name,
                'type': 'bar',
                'barGap': '0',
                # 'label': labelOption,
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

    def gen_options(self):
        x = list(self.data.astype(str)['x'].unique())
        ys = dict()
        stacks = self.data['stacks']
        groups = list(stacks.unique())
        for name, s in self.data.groupby(stacks):
            y = list(s['y'])
            ys[name] = y
    
        series_list = list()

        for name, y in ys.items():
            d = {
                'name': name,
                'type': 'bar',
                'barGap': '0',
                # 'label': labelOption,
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





        