#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用基础数据结构实现 LRU Cache

LRU (Least Recently Used) Cache 是一种缓存淘汰策略，当缓存达到容量上限时，
会淘汰最近最少使用的数据。

实现原理：
1. 使用双向链表维护数据的使用顺序（最近使用的在头部，最少使用的在尾部）
2. 使用哈希表（字典）实现 O(1) 时间复杂度的查找
3. 当插入新数据时，如果缓存已满，则删除尾部节点（最少使用的数据）
"""

class ListNode:
    """双向链表节点类"""
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """LRU Cache 实现类"""
    
    def __init__(self, capacity):
        """
        初始化 LRU Cache
        
        Args:
            capacity: 缓存容量
        """
        self.capacity = capacity
        self.cache = {}  # 哈希表，存储 key 到链表节点的映射
        
        # 创建虚拟头节点和尾节点
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """
        在链表头部添加节点（最近使用的节点）
        
        Args:
            node: 要添加的节点
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """
        从链表中移除节点
        
        Args:
            node: 要移除的节点
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """
        将节点移动到链表头部（表示最近使用）
        
        Args:
            node: 要移动的节点
        """
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """
        移除并返回链表尾部的节点（最少使用的节点）
        
        Returns:
            ListNode: 被移除的节点
        """
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node
    
    def get(self, key):
        """
        获取缓存中的值
        
        Args:
            key: 键
            
        Returns:
            int: 对应的值，如果键不存在返回 -1
        """
        if key not in self.cache:
            return -1
        
        # 获取节点并移动到头部（表示最近使用）
        node = self.cache[key]
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
        """
        插入或更新缓存中的键值对
        
        Args:
            key: 键
            value: 值
        """
        if key in self.cache:
            # 键已存在，更新值并移动到头部
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 创建新节点
            new_node = ListNode(key, value)
            
            # 添加到缓存和链表头部
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # 如果超过容量，移除最少使用的节点
            if len(self.cache) > self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
    
    def delete(self, key):
        """
        删除缓存中的键值对
        
        Args:
            key: 要删除的键
            
        Returns:
            bool: 是否成功删除
        """
        if key not in self.cache:
            return False
        
        node = self.cache[key]
        self._remove_node(node)
        del self.cache[key]
        return True
    
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
        # 重置链表
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get_all_items(self):
        """
        获取缓存中的所有键值对（按使用顺序从最近到最旧）
        
        Returns:
            list: 键值对列表
        """
        items = []
        current = self.head.next
        while current != self.tail:
            items.append((current.key, current.value))
            current = current.next
        return items
    
    def __str__(self):
        """
        返回 LRU Cache 的字符串表示
        
        Returns:
            str: LRU Cache 的字符串表示
        """
        items = []
        current = self.head.next
        while current != self.tail:
            items.append("{}: {}".format(current.key, current.value))
            current = current.next
        return "LRUCache({})".format(" -> ".join(items))
    
    def __repr__(self):
        """
        返回 LRU Cache 的详细字符串表示
        
        Returns:
            str: LRU Cache 的详细字符串表示
        """
        return "LRUCache(capacity={}, size={})".format(self.capacity, len(self.cache))


def test_lru_cache():
    """
    测试 LRU Cache 的功能
    """
    print("=== LRU Cache 功能测试 ===")
    
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
    print("获取 key=4: {}".format(lru.get(4)))  # 应该返回 -1（不存在）
    print("LRU Cache 使用顺序: {}".format(lru))
    
    # 测试 LRU 淘汰策略
    print("\n3. 测试 LRU 淘汰策略:")
    lru.put(4, "D")  # 插入新数据，应该淘汰 key=2（因为 key=1 最近被使用）
    print("插入 key=4 后: {}".format(lru))
    print("获取 key=2: {}".format(lru.get(2)))  # 应该返回 -1（已被淘汰）
    
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
    print("get(2): {}".format(lru.get(2)))  # 返回 -1
    lru.put(4, 4)  # 淘汰 key=1
    print("get(1): {}".format(lru.get(1)))  # 返回 -1
    print("get(3): {}".format(lru.get(3)))  # 返回 3
    print("get(4): {}".format(lru.get(4)))  # 返回 4
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_lru_cache()