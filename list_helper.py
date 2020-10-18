"""
定义对所有容器和可迭代对象的操作
"""


class ListHelper():
    """
      列表助手
    """

    @staticmethod
    def find_all(iteratble_target, func_condition):
        """
        在可迭代对象中，查找符合条件的多个元素
        :param iteratble_target: 可迭代对象
        :param func_condition: 所有条件
        :return:生成器对象
        """
        for item in iteratble_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_one(iteratble_target, func_condition):
        """
        在可迭代对象中查找一个符合所有条件的元素
        :param iteratble_target: 可迭代对象
        :param func_condition: 所有条件
        :return: 元素
        """
        for item in iteratble_target:
            if func_condition(item):
                return item

    @staticmethod
    def sum_all(iterable_target,func_condition):
        """
        计算可迭代元素中，符合条件的元素总和
        :param iterable_target:可迭代对象
        :param func_condition: 求和条件
        :return: 元素总和数值
        """
        sum = 0
        for item in iterable_target:
            data = func_condition(item)
            sum += data
        return sum

    @staticmethod
    def max_one(iterable_target,func_condition):
        """
        根据条件，计算可迭代对象中最大的元素
        :param iterable_target: 可迭代对象
        :param func_condition: 最大条件
        :return: 最大元素
        """
        max_item = iterable_target[0]
        for item in iterable_target:
            if func_condition(item) > func_condition(max_item):
                max_item = item
        return max_item

    @staticmethod
    def select(iterable_target, func_condition):
        """
        根据条件，选择可迭代对象符合的对象属性
        :param iterable_target: 可迭代对象
        :param func_condition: 筛选条件
        :return: 对象属性
        """
        for item in iterable_target:
            yield func_condition(item)

    @staticmethod
    def sort_low_to_high(iterable_target, func_condition):
        """
        根据条件，根据条件排序可迭代对象中的元素
        :param iterable_target: 可迭代对象
        :param func_condition: 排序条件
        :return: 生成器对象
        """
        for index in range(len(iterable_target)-1):
            for s in range(index+1,len(iterable_target)):
                if func_condition(iterable_target[index]) > func_condition(iterable_target[s]):
                    iterable_target[index],iterable_target[s] = iterable_target[s],iterable_target[index]
            #不需要return或者yiel，因为ierable指向的是可迭代对象，函数中操作可变数据，可以改变数据

    @staticmethod
    def min_one(iterable_target, func_condition):
        """
        根据条件，计算可迭代对象中最小的元素
        :param iterable_target: 可迭代对象
        :param func_condition: 最小条件
        :return: 最小元素
        """
        min_item = iterable_target[0]
        for item in iterable_target:
            if func_condition(item) < func_condition(min_item):
                min_item = item
        return min_item

    @staticmethod
    def sort_high_to_low(iterable_target, func_condition):
        """
        根据条件，根据条件降序排序可迭代对象中的元素
        :param iterable_target: 可迭代对象
        :param func_condition: 排序条件
        :return: 生成器对象
        """
        for index in range(len(iterable_target) - 1):
            for s in range(index + 1, len(iterable_target)):
                if func_condition(iterable_target[index]) < func_condition(iterable_target[s]):
                    iterable_target[index], iterable_target[s] = iterable_target[s], iterable_target[index]
            # 不需要return或者yiel，因为ierable指向的是列表，函数中操作列表，可以改变列表

    @staticmethod
    def remove(iterable_target, func_condition):
        """
        根据条件，删除可变可迭代对象中的元素
        :param iterable_target: 可迭代对象
        :param func_condition: 删除条件
        :return: None
        """
        for item in iterable_target:
            if func_condition(item):
                iterable_target.remove(item)