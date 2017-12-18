#! /usr/bin/env python3
import json
from datetime import datetime as dt
from collections import namedtuple

def calculate_scores():
    with open('leaderboard.json', 'r') as f:
        data = json.loads(f.read())['members']
    Result = namedtuple('Result', ['Name', 'Day', 'DeltaT'])
    TimeResults = []
    for competitor in data.items():
        for day in competitor[1]['completion_day_level'].items():
            if day[1]['2']:
                difftime = dt.strptime(day[1]['2']['get_star_ts'], '%Y-%m-%dT%H:%M:%S%z') - \
                    dt.strptime(day[1]['1']['get_star_ts'], '%Y-%m-%dT%H:%M:%S%z')
                TimeResults.append(
                    Result(competitor[1]['name'], int(day[0]), difftime))
    unique_competitors = set(result.Name for result in TimeResults)
    total_points = dict.fromkeys(unique_competitors, 0)
    for i in range(1, max(result.Day for result in TimeResults)+1):
        ordered_list = sorted((result for result in TimeResults if result.Day == i),
                key=lambda x: x.DeltaT)
        for j, item in enumerate(ordered_list):
            total_points[item.Name] += len(unique_competitors) - j
    return sorted(total_points.items(), key = lambda x: x[1], reverse=True)

def print_scores(sorted_scores):
    # Reverse order printing- Person : Score
    # longest_name = max(len(competitor[0]) for competitor in sorted_scores)
    # for k,v in sorted_scores:
        # print('{} : {:{}}'.format(v, k, longest_name))
    print('')
    for k,v in sorted_scores:
        print('{:>7} : {}'.format(v, k))
    print('')

if __name__ == '__main__':
    print_scores(calculate_scores())