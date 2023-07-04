# Learning Project: 0x01 Lockboxes Algorithm (Python)

Welcome to the learning project on the Lockboxes algorithm using Python! In this project, we will explore the Lockboxes problem and develop an algorithm to solve it efficiently. This project aims to enhance your understanding of algorithms and problem-solving techniques.

## Table of Contents
- [Introduction](#introduction)
- [Problem Description](#problem-description)
- [Algorithm](#algorithm)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Lockboxes algorithm is a classic problem in computer science that involves unlocking a series of locked boxes. Each box may contain keys to other boxes, and the goal is to determine if all boxes can be unlocked. This problem requires a systematic approach to traversal and exploration of the box-key relationships.

In this learning project, we will implement an algorithm in Python to solve the Lockboxes problem efficiently. By understanding and solving this problem, you will strengthen your algorithmic thinking and problem-solving skills.

## Problem Description

Given a list of lockboxes represented as a 2D list, where each inner list contains the keys present in a box, the task is to determine if all the lockboxes can be opened. A lockbox can be opened if it contains the key to another lockbox, directly or indirectly.

The problem can be solved by performing a depth-first search (DFS) or breadth-first search (BFS) traversal on the lockboxes. By keeping track of the opened boxes and the keys obtained, we can explore the box-key relationships and check if all boxes can be opened.

## Algorithm

To solve the Lockboxes problem, we can follow these steps:

1. Create a list or set to keep track of the opened boxes.
2. Start with the initial box (box 0) and add it to the opened boxes list.
3. For each key in box 0, check if the corresponding box is already opened:
   - If the box is already opened, continue to the next key.
   - If the box is not opened, add it to the opened boxes list and recursively perform the same steps for that box.
4. Repeat the above steps until all boxes have been explored or until no new boxes can be opened.
5. After exploring all the boxes, check if the number of opened boxes is equal to the total number of boxes. If it is, return True; otherwise, return False.

The algorithm can be implemented using a recursive function or an iterative approach using a stack or queue data structure.

## Examples

Here are some example scenarios of the Lockboxes problem:

- Example 1:

  Input:
  ```python
  boxes = [
      [1],      # Box 0 contains the key to Box 1
      [2],      # Box 1 contains the key to Box 2
      [3],      # Box 2 contains the key to Box 3
      []        # Box 3 does not contain any keys
  ]

  print(can_unlock_all_boxes(boxes))
