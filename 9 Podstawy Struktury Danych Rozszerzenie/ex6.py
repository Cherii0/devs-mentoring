data = {
    "data": [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': { 'analysis_1': [1, 10, 15, 120.2, '120'], 'analysis_2': [10, 100, "test", 200, 300]},
    'probes': [["probe_1", "probe_2"], "probe_3"]
}

result = []


for d in data.keys():
    if d == "data":
        for elem in data[d]:
            if type(elem) == str:
                result.append(elem)

    elif d == "nested_analysis":
        for d2 in data[d].keys():
            for elem in data[d][d2]:
                if type(elem) == str:
                    result.append(elem)

    else:
        for elem in data[d]:
            if type(elem) == str:
                result.append(elem)
            else:
                result.extend(elem)

# poprawny wynik dla porownania
print(['asd','120',"test", "probe_1", "probe_2","probe_3" ])
print(result)
