

class BarplotSimple():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x_col = self.data.columns[0]
        y_col = self.data.columns[1]

        x = list(self.data[x_col])
        y = list(self.data[y_col])

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
                'type': 'value',
                'name': f'{self.metadata[y_col]["label"]} in {self.metadata[y_col]["unit"]}',
                'nameLocation': 'middle',
                'nameGap': 50
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
        x_col = self.data.columns[0]
        y_col = self.data.columns[1]
        g_col = self.data.columns[2]

        x = list(self.data[x_col].astype(str).unique())

        series_list = list()
        groups = list(self.data[g_col].unique())
        for selection, s in self.data.groupby(g_col):
            y = list(s[y_col])
            d = {
                'name': selection,
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
                'type': 'value',
                'name': f'{self.metadata[y_col]["label"]} in {self.metadata[y_col]["unit"]}',
                'nameLocation': 'middle',
                'nameGap': 50
            },
            'series': series_list
        }

        return options
    

class BarplotStacked():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x_col = self.data.columns[0]
        y_col = self.data.columns[1]
        s_col = self.data.columns[2]

        series_list = list()
        x = list(self.data.astype(str)[x_col].unique())
        stacks = list(self.data[s_col].unique())
        for selection, s in self.data.groupby(s_col):
            y = list(s[y_col])
            d = {
                'name': selection,
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
                'data': stacks
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value',
                'name': f'{self.metadata[y_col]["label"]} in {self.metadata[y_col]["unit"]}',
                'nameLocation': 'middle',
                'nameGap': 50
            },
            'series': series_list
        }

        return options
    

class BarplotGroupedStacked():

    def __init__(self, data, metadata=None):
        self.data = data
        self.metadata = metadata

    def build_options(self):
        x_col = self.data.columns[0]
        y_col = self.data.columns[1]
        g_col = self.data.columns[2]
        s_col = self.data.columns[3]

        x = list(self.data[x_col].astype(str).unique())
        stacks = list(self.data[s_col].unique())
        series_list = list()
        for selection, s in self.data.groupby([g_col, s_col]):
            group_name = selection[0]
            stack_name = selection[1]
            y = list(s[y_col])
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
        
        options = {
            'tooltip': {
                'trigger': 'axis',
                'axisPointer': {
                'type': 'shadow'
                }
            },
            'legend': {
                'data': stacks
            },
            'xAxis': {
                'type': 'category',
                'data': x
            },
            'yAxis': {
                'type': 'value',
                'name': f'{self.metadata[y_col]["label"]} in {self.metadata[y_col]["unit"]}',
                'nameLocation': 'middle',
                'nameGap': 50
            },
            'series': series_list
        }

        return options





        