with open ("log.txt") as f:
    for line in f:
        event_time, operation, key, event_type = line.split(' ')
        assert operation == 'Operation'
        if event_type == 'Start':
            key.start.append(event_time)
            