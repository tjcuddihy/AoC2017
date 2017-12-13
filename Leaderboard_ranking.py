import argparse
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime as dt


def main(args=None):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # top-level commands
    parser.add_argument('-d', '--day',
                        help='Which day would you like to view a plot for? Defaults to most recent.')
    parser.add_argument('-j', '--json', default='leaderboard.json',
                        help='Name of the file containing the json dump')

    options, unknowns = parser.parse_known_args(args)
    day = options.day

    # Dict of the start times for each day of the Advent. Used for difftiming
    start_times = {'1': '2017-12-01T00:00:00-0500', '2': '2017-12-02T00:00:00-0500', '3': '2017-12-03T00:00:00-0500', '4': '2017-12-04T00:00:00-0500', '5': '2017-12-05T00:00:00-0500', '6': '2017-12-06T00:00:00-0500', '7': '2017-12-07T00:00:00-0500', '8': '2017-12-08T00:00:00-0500', '9': '2017-12-09T00:00:00-0500', '10': '2017-12-10T00:00:00-0500', '11': '2017-12-11T00:00:00-0500', '12': '2017-12-12T00:00:00-0500',
                   '13': '2017-12-13T00:00:00-0500', '14': '2017-12-14T00:00:00-0500', '15': '2017-12-15T00:00:00-0500', '16': '2017-12-16T00:00:00-0500', '17': '2017-12-17T00:00:00-0500', '18': '2017-12-18T00:00:00-0500', '19': '2017-12-19T00:00:00-0500', '20': '2017-12-20T00:00:00-0500', '21': '2017-12-21T00:00:00-0500', '22': '2017-12-22T00:00:00-0500', '23': '2017-12-23T00:00:00-0500', '24': '2017-12-24T00:00:00-0500', '25': '2017-12-25T00:00:00-0500'}

    with open(options.json, 'r') as f:
        data = json.loads(f.read())['members']

    completions = []  # completion -> Name | Puzzle | Part 1 or 2 | TimeStamp
    for member in data:
        for puzzle in data[member]['completion_day_level']:
            for part in data[member]['completion_day_level'][puzzle]:
                difftime = dt.strptime(data[member]['completion_day_level'][puzzle][part]['get_star_ts'],
                                       '%Y-%m-%dT%H:%M:%S%z') - dt.strptime(start_times[puzzle], '%Y-%m-%dT%H:%M:%S%z')
                completions.append([data[member]['name'],
                                    puzzle,
                                    part,
                                    difftime])

    if day is None:
        day = str(max(int(_[1]) for _ in completions))
    if day not in set(_[1] for _ in completions):
        raise ValueError(
            'Day {} not available in json data. Update leaderboard.json'.format(day))

    results = [_ for _ in completions if _[1] == day]
    competitors = [_[0] for _ in results if _[2] == '1']

    y_pos = np.arange(len(competitors))
    times = np.array([[_[3].seconds / 60 for _ in results if _[2] == '1'],
                      [_[3].seconds / 60 for _ in results if _[2] == '2']])

    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.plot(times[0], y_pos, 'ko', markersize=3)
    ax.plot(times[1], y_pos, 'k+', markersize=4)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(competitors)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Minutes after release')
    ax.set_title('Completion Time - Day {}'.format(day))
    plt.show()


if __name__ == '__main__':
    main()
