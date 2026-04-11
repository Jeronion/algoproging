class TypeStatistics:
    def __init__(self, lst):
        self.lst = lst
    
    def type_values(self):
        result = {}
        for item in self.lst:
            type_name = item.__class__.__name__
            if type_name not in result:
                result[type_name] = []
            result[type_name].append(item)
        return result
    
    def type_counts(self):
        result = {}
        for item in self.lst:
            type_name = item.__class__.__name__
            result[type_name] = result.get(type_name, 0) + 1
        return result