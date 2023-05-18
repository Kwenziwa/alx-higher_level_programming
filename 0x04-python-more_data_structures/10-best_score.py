#!/usr/bin/python3
def best_score(dict):
    return max(dict, key=dict.get) if dict else None
