#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/10/14 15:02
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/10/14 15:02
 * @Desc:
"""


from typing import List, Dict, Union, Optional, Any


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    广度优先遍历
    :param graph: 图节点列表
    :param start: 头结点
    :return: 遍历结果列表
    """
    queue = [start]
    seen = set()
    seen.add(start)
    res = []
    while len(queue) > 0:
        # 顶点
        vertex = queue.pop(0)
        # 顶点的临接元素
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                # 将子节点入队
                queue.append(node)
                # 标记访问过的节点
                seen.add(node)
        print("当前访问的元素: ", vertex)
        res.append(vertex)
    return res


def bfs_short_path(graph: Dict[str, List[str]], start: str) -> Dict[str, Union[Optional[str], Any]]:
    """
   广度优先遍历求最短路径
   :param graph: 图节点列表
   :param start: 头结点
   :return: 遍历结果列表
    """
    queue = [start]
    seen = set()
    seen.add(start)
    # 记录父节点
    parent = {start: None}
    while len(queue) > 0:
        # 顶点
        vertex = queue.pop(0)
        # parent[start] = vertex
        # 顶点的临接元素
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                # 将子节点入队
                queue.append(node)
                # 标记访问过的节点
                seen.add(node)
                parent[node] = vertex
    while start:
        print(start, end='->')
        start = parent[start]
    print('end')
    return parent


if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }
    print(bfs(graph, 'A'))
    print(bfs_short_path(graph, 'A'))
