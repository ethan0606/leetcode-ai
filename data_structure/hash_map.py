#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用基础数据结构实现 HashMap

HashMap 是一种基于哈希表实现的键值对数据结构，支持 O(1) 平均时间复杂度的插入、查找和删除操作。
"""

class HashMap:
    """
    使用数组和链表实现的 HashMap
    
    实现原理：
    1. 使用哈希函数将键映射到数组索引
    2. 使用链表处理哈希冲突（链地址法）
    3. 动态扩容以保持性能
    """
    
    def __init__(self, capacity=16, load_factor=0.75):
        """
        初始化 HashMap
        
        Args:
            capacity: 初始容量，必须是2的幂
            load_factor: 负载因子，当元素数量达到 capacity * load_factor 时扩容
        """
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        """
        哈希函数：将键转换为数组索引
        
        Args:
            key: 键
            
        Returns:
            int: 数组索引
        """
        # 使用 Python 内置的 hash 函数，然后取模
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """
        插入或更新键值对
        
        Args:
            key: 键
            value: 值
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # 检查键是否已存在
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # 键已存在，更新值
                bucket[i] = (key, value)
                return
        
        # 键不存在，添加新键值对
        bucket.append((key, value))
        self.size += 1
        
        # 检查是否需要扩容
        if self.size > self.capacity * self.load_factor:
            self._resize()
    
    def get(self, key, default=None):
        """
        根据键获取值
        
        Args:
            key: 键
            default: 键不存在时返回的默认值
            
        Returns:
            对应的值或默认值
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return default
    
    def delete(self, key):
        """
        删除键值对
        
        Args:
            key: 要删除的键
            
        Returns:
            bool: 是否成功删除
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False
    
    def contains_key(self, key):
        """
        检查键是否存在
        
        Args:
            key: 要检查的键
            
        Returns:
            bool: 键是否存在
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return True
        
        return False
    
    def keys(self):
        """
        返回所有键的列表
        
        Returns:
            list: 所有键的列表
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)
        return result
    
    def values(self):
        """
        返回所有值的列表
        
        Returns:
            list: 所有值的列表
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(v)
        return result
    
    def items(self):
        """
        返回所有键值对的列表
        
        Returns:
            list: 所有键值对的列表
        """
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result
    
    def _resize(self):
        """
        扩容哈希表
        
        当元素数量超过负载因子时，将容量翻倍并重新哈希所有元素
        """
        # 保存当前所有元素
        old_items = self.items()
        
        # 扩容
        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        
        # 重新插入所有元素
        for key, value in old_items:
            self.put(key, value)
    
    def __len__(self):
        """
        返回 HashMap 的大小
        
        Returns:
            int: 元素数量
        """
        return self.size
    
    def __contains__(self, key):
        """
        支持 in 操作符
        
        Args:
            key: 要检查的键
            
        Returns:
            bool: 键是否存在
        """
        return self.contains_key(key)
    
    def __getitem__(self, key):
        """
        支持 [] 操作符获取值
        
        Args:
            key: 键
            
        Returns:
            对应的值
            
        Raises:
            KeyError: 键不存在时抛出异常
        """
        value = self.get(key)
        if value is None:
            raise KeyError("Key '{}' not found".format(key))
        return value
    
    def __setitem__(self, key, value):
        """
        支持 [] 操作符设置值
        
        Args:
            key: 键
            value: 值
        """
        self.put(key, value)
    
    def __delitem__(self, key):
        """
        支持 del 操作符删除键值对
        
        Args:
            key: 要删除的键
            
        Raises:
            KeyError: 键不存在时抛出异常
        """
        if not self.delete(key):
            raise KeyError("Key '{}' not found".format(key))
    
    def __str__(self):
        """
        返回 HashMap 的字符串表示
        
        Returns:
            str: HashMap 的字符串表示
        """
        items = []
        for bucket in self.buckets:
            for k, v in bucket:
                items.append("{}: {}".format(k, v))
        return "{" + ", ".join(items) + "}"
    
    def __repr__(self):
        """
        返回 HashMap 的详细字符串表示
        
        Returns:
            str: HashMap 的详细字符串表示
        """
        return "HashMap(capacity={}, size={})".format(self.capacity, self.size)


def test_hash_map():
    """
    测试 HashMap 的功能
    """
    print("=== HashMap 功能测试 ===")
    
    # 创建 HashMap
    hm = HashMap()
    
    # 测试插入操作
    print("\n1. 插入键值对:")
    hm.put("name", "Alice")
    hm.put("age", 30)
    hm.put("city", "New York")
    hm["country"] = "USA"  # 使用 [] 操作符
    print("HashMap: {}".format(hm))
    print("大小: {}".format(len(hm)))
    
    # 测试获取操作
    print("\n2. 获取值:")
    print("name: {}".format(hm.get('name')))
    print("age: {}".format(hm['age']))  # 使用 [] 操作符
    print("不存在的键: {}".format(hm.get('gender', 'Unknown')))
    
    # 测试检查键是否存在
    print("\n3. 检查键是否存在:")
    print("'name' in hm: {}".format('name' in hm))
    print("'gender' in hm: {}".format('gender' in hm))
    
    # 测试更新操作
    print("\n4. 更新值:")
    hm.put("age", 31)
    hm["city"] = "Boston"
    print("更新后的 HashMap: {}".format(hm))
    
    # 测试删除操作
    print("\n5. 删除键值对:")
    hm.delete("city")
    del hm["country"]  # 使用 del 操作符
    print(f"删除后的 HashMap: {hm}")
    print(f"大小: {len(hm)}")
    
    # 测试遍历操作
    print("\n6. 遍历操作:")
    print(f"所有键: {hm.keys()}")
    print(f"所有值: {hm.values()}")
    print(f"所有键值对: {hm.items()}")
    
    # 测试扩容
    print("\n7. 测试扩容:")
    large_hm = HashMap(capacity=4, load_factor=0.75)
    for i in range(10):
        large_hm.put(f"key{i}", f"value{i}")
    print(f"扩容后的 HashMap: {large_hm}")
    print(f"容量: {large_hm.capacity}")
    print(f"大小: {len(large_hm)}")
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_hash_map()