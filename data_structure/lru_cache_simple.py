#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简化版 LRU Cache 实现

使用列表维护使用顺序，虽然时间复杂度不是最优的 O(1)，但实现简单易懂。
"""

class LRUCache:
    """LRU Cache 实现类"""
    
    def __init__(self, capacity):
        """
        初始化 LRU Cache
        
        Args:
            capacity: 缓存容量
        """
        self.capacity = capacity
        self.cache = {}  # 哈希表，存储 key 到值的映射
        self.order = []  # 用于维护键的使用顺序（最近使用的在末尾）

    def put(self, key, value):
        """
        插入或更新键值对
        
        Args:
            key: 键
            value: 值
            
        Returns:
            bool: 操作是否成功
        """
        if key in self.cache:
            # 键已存在，更新值并移动到最近使用位置
            self.cache[key] = value
            self.order.remove(key)  # 从原位置移除
            self.order.append(key)  # 添加到末尾（最近使用）
        else:
            # 键不存在，插入新键值对
            self.cache[key] = value
            self.order.append(key)
            
            # 检查是否超过容量
            if len(self.cache) > self.capacity:
                # 移除最久未使用的键（列表第一个元素）
                oldest_key = self.order[0]
                self.cache.pop(oldest_key)
                self.order.pop(0)
        
        return True

    def get(self, key):
        """
        获取键对应的值
        
        Args:
            key: 键
            
        Returns:
            对应的值，如果键不存在返回 None
        """
        if key in self.cache:
            # 键存在，移动到最近使用位置并返回值
            self.order.remove(key)  # 从原位置移除
            self.order.append(key)  # 添加到末尾（最近使用）
            return self.cache[key]
        else:
            # 键不存在，返回 None
            return None
    
    def delete(self, key):
        """
        删除键值对
        
        Args:
            key: 要删除的键
            
        Returns:
            bool: 是否成功删除
        """
        if key in self.cache:
            # 键存在，删除键值对
            self.cache.pop(key)
            self.order.remove(key)
            return True
        else:
            # 键不存在，返回 False
            return False
    
    def contains(self, key):
        """
        检查键是否存在于缓存中
        
        Args:
            key: 要检查的键
            
        Returns:
            bool: 键是否存在
        """
        return key in self.cache
    
    def size(self):
        """
        返回当前缓存的大小
        
        Returns:
            int: 缓存大小
        """
        return len(self.cache)
    
    def is_full(self):
        """
        检查缓存是否已满
        
        Returns:
            bool: 缓存是否已满
        """
        return len(self.cache) >= self.capacity
    
    def clear(self):
        """清空缓存"""
        self.cache.clear()
        self.order = []  # 兼容 Python 2.x，列表没有 clear() 方法
    
    def get_all_items(self):
        """
        获取缓存中的所有键值对（按使用顺序从最旧到最新）
        
        Returns:
            list: 键值对列表
        """
        items = []
        for key in self.order:
            items.append((key, self.cache[key]))
        return items
    
    def __str__(self):
        """
        返回 LRU Cache 的字符串表示
        
        Returns:
            str: LRU Cache 的字符串表示
        """
        items = []
        for key in self.order:
            items.append("{}: {}".format(key, self.cache[key]))
        return "LRUCache({})".format(" -> ".join(items))
    
    def __repr__(self):
        """
        返回 LRU Cache 的详细字符串表示
        
        Returns:
            str: LRU Cache 的详细字符串表示
        """
        return "LRUCache(capacity={}, size={})".format(self.capacity, len(self.cache))


def test_lru_cache_simple():
    """
    测试简化版 LRU Cache 的功能
    """
    print("=== 简化版 LRU Cache 功能测试 ===")
    
    # 创建容量为 3 的 LRU Cache
    lru = LRUCache(3)
    
    # 测试插入操作
    print("\n1. 插入键值对:")
    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    print("LRU Cache: {}".format(lru))
    print("大小: {}".format(lru.size()))
    print("是否已满: {}".format(lru.is_full()))
    
    # 测试获取操作
    print("\n2. 获取值:")
    print("获取 key=1: {}".format(lru.get(1)))  # 应该返回 "A"
    print("获取 key=4: {}".format(lru.get(4)))  # 应该返回 None（不存在）
    print("LRU Cache 使用顺序: {}".format(lru))
    
    # 测试 LRU 淘汰策略
    print("\n3. 测试 LRU 淘汰策略:")
    lru.put(4, "D")  # 插入新数据，应该淘汰 key=2（因为 key=1 最近被使用）
    print("插入 key=4 后: {}".format(lru))
    print("获取 key=2: {}".format(lru.get(2)))  # 应该返回 None（已被淘汰）
    
    # 测试更新操作
    print("\n4. 测试更新操作:")
    lru.put(3, "C-updated")  # 更新现有键的值
    print("更新 key=3 后: {}".format(lru))
    print("获取 key=3: {}".format(lru.get(3)))  # 应该返回 "C-updated"
    
    # 测试删除操作
    print("\n5. 测试删除操作:")
    lru.delete(1)
    print("删除 key=1 后: {}".format(lru))
    print("大小: {}".format(lru.size()))
    
    # 测试检查操作
    print("\n6. 测试检查操作:")
    print("包含 key=3: {}".format(lru.contains(3)))
    print("包含 key=1: {}".format(lru.contains(1)))
    
    # 测试清空操作
    print("\n7. 测试清空操作:")
    lru.clear()
    print("清空后: {}".format(lru))
    print("大小: {}".format(lru.size()))
    
    # 测试复杂场景
    print("\n8. 测试复杂场景:")
    lru = LRUCache(2)
    
    # 操作序列：put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)
    lru.put(1, 1)
    lru.put(2, 2)
    print("get(1): {}".format(lru.get(1)))  # 返回 1
    lru.put(3, 3)  # 淘汰 key=2
    print("get(2): {}".format(lru.get(2)))  # 返回 None
    lru.put(4, 4)  # 淘汰 key=1
    print("get(1): {}".format(lru.get(1)))  # 返回 None
    print("get(3): {}".format(lru.get(3)))  # 返回 3
    print("get(4): {}".format(lru.get(4)))  # 返回 4
    
    # 测试边界情况
    print("\n9. 测试边界情况:")
    lru = LRUCache(0)
    lru.put(1, "A")  # 容量为0，应该无法插入
    print("容量为0时的缓存: {}".format(lru))
    print("大小: {}".format(lru.size()))
    
    # 测试重复插入相同键
    print("\n10. 测试重复插入相同键:")
    lru = LRUCache(3)
    lru.put(1, "A")
    lru.put(1, "A-updated")
    lru.put(2, "B")
    lru.put(1, "A-final")  # 多次更新同一个键
    print("重复插入后的缓存: {}".format(lru))
    print("获取 key=1: {}".format(lru.get(1)))
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_lru_cache_simple()