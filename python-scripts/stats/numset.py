import utils

class NumSet:
    def __init__(self, numbers):
        self.nums = numbers
        self.nums_sorted = sorted(numbers)
        self.n = len(numbers)

    def _mean(self):
        average = 0
        for num in self.nums:
            average += num
        average = average / self.n
        return average
    
    def mean(self):
        average = self._mean()
        msg = f'Average: {average}'
        utils.fancy_print(msg)
        return average
    
    def mad(self):
        average = self._mean()
        numerator = 0
        for num in self.nums:
            x = (num - average)
            if x < 0: x *= -1
            numerator += x
        mean_abs_dev = numerator / self.n
        msg = f'Mean Absolute Deviation: {mean_abs_dev}'
        utils.fancy_print(msg)
        return mean_abs_dev
    
    def _median(self, arr=None):
        if arr is None:
            arr = self.nums_sorted
        n = len(arr)
        mid = n // 2

        if n % 2 == 1:
            median = arr[mid]
        else: 
            median = (arr[mid - 1] + arr[mid]) / 2
        return median

    def median(self):
        self.sort_nums()    # print sorted list
        median = self._median()
        msg = f'Median: {median}'
        utils.fancy_print(msg)
        return median
    
    def _five_num_summary(self):
        summary = [0] * 5
        summary[0] = self.nums_sorted[0]
        summary[2] = self._median()
        summary[4] = self.nums_sorted[self.n - 1]
        
        mid = self.n // 2
        if self.n % 2 == 1:
            summary[1] = self._median(arr=self.nums_sorted[:mid])
            summary[3] = self._median(arr=self.nums_sorted[mid + 1:])
        else:
            summary[1] = self._median(arr=self.nums_sorted[:mid])
            summary[3] = self._median(arr=self.nums_sorted[mid:])
        return summary
    
    def five_num_summary(self):
        summary = self._five_num_summary()
        utils.fancy_print('Five-number Summary')
        self.sort_nums()
        utils.fancy_print(f'Min: {summary[0]}')
        utils.fancy_print(f'Q1: {summary[1]}')
        utils.fancy_print(f'Median: {summary[2]}')
        utils.fancy_print(f'Q3: {summary[3]}')
        utils.fancy_print(f'Max: {summary[4]}')

    def _iqr(self):
        summary = self._five_num_summary()
        return summary[3] - summary[1]

    def _outlier_scale(self):
        return 1.5 * self._iqr()
    
    def iqr_outlier(self):
        outlier = self._outlier_scale()
        five_num = self._five_num_summary()
        iqr = self._iqr()
        lower = five_num[1] - outlier
        upper = five_num[3] + outlier
        utils.fancy_print(f'Interquartile Range: {iqr}')
        utils.fancy_print(f'Outliers: values < {lower} and values > {upper}')
        
    def mode(self):
        frequency_table = {}
        for num in self.nums:
            if num in frequency_table:
                frequency_table[num] += 1
            else:
                frequency_table[num] = 1
        
        most = max(frequency_table.values)
        mode = []
        for k, v in frequency_table.items():
            if v == most:
                mode.append(k)
        
        if len(mode) == 1:
            msg = f'Mode: {mode[0]}'
            utils.fancy_print(msg)
            return mode[0]
        elif len(mode) == self.n:
            msg = 'No mode.'
            utils.fancy_print(msg)
            return
        else:
            msg = 'Modes: ' + ', '.join(map(str, mode))
            utils.fancy_print(msg)
            return mode

    def _variance(self, ntype):
        numerator = 0
        mean = self._mean()
        for num in self.nums:
            each = num - mean
            each = each ** 2
            numerator += each
        
        if ntype == 'sample':
            n = self.n - 1
        elif ntype == 'population':
            n = self.n
        else:
            utils.fancy_print("Please input 'sample' or 'population' for type!")
            return
        return numerator / n
    
    def variance(self, ntype):
        variance = self._variance(ntype)
        if variance is None:
            return
        
        msg = f'{ntype.capitalize()} Variance: {variance}'
        utils.fancy_print(msg)
        return variance

    def stddev(self, ntype):
        stddev_res = self._variance(ntype)
        if stddev_res is None:
            return
        
        stddev_res = stddev_res ** 0.5
        msg = f'{ntype.capitalize()} Standard Deviation: {stddev_res}'
        utils.fancy_print(msg)
        return stddev_res
    
    def sort_nums(self):
        msg = 'Sorted list: ' + ', '.join(map(str, self.nums_sorted))
        utils.fancy_print(msg)

    def mean_based(self):
        utils.fancy_print('Summary of Dataset Statistics')
        self.sort_nums()
        self.mean()
        self.mad()
        self.variance('sample')
        self.stddev('sample')
        self.variance('population')
        self.stddev('population')

    def median_based(self):
        utils.fancy_print('Summary of Dataset Statistics')
        self.median()
        self.five_num_summary()
        self.iqr_outlier()