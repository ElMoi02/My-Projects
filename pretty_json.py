data = [
    {"word": "open", "score": 1001}, {"word": "great", "score": 1000},
    {"word": "vast", "score": 999}, {"word": "deep", "score": 998},
    {"word": "western", "score": 997}, {"word": "atlantic", "score": 996},
    {"word": "wide", "score": 995}, {"word": "indian", "score": 994},
    {"word": "blue", "score": 993}, {"word": "southern", "score": 992},
    {"word": "eastern", "score": 991}, {"word": "whole", "score": 990},
    {"word": "mighty", "score": 989}, {"word": "boundless", "score": 988},
    {"word": "tropical", "score": 987}, {"word": "northern", "score": 986},
    {"word": "broad", "score": 985}, {"word": "dark", "score": 984},
    {"word": "stormy", "score": 983}, {"word": "infinite", "score": 982},
    {"word": "entire", "score": 981}, {"word": "central", "score": 980},
    {"word": "upper", "score": 979}, {"word": "equatorial", "score": 978},
    {"word": "inter", "score": 977}, {"word": "north", "score": 976},
    {"word": "coastal", "score": 975}, {"word": "distant", "score": 974},
    {"word": "unknown", "score": 973}, {"word": "mid", "score": 972},
    {"word": "immense", "score": 971}, {"word": "lndian", "score": 970},
    {"word": "global", "score": 969}, {"word": "big", "score": 968},
    {"word": "primeval", "score": 967}, {"word": "warm", "score": 966},
    {"word": "wild", "score": 965}, {"word": "frozen", "score": 964},
    {"word": "endless", "score": 963}, {"word": "green", "score": 962},
    {"word": "german", "score": 961}, {"word": "shoreless", "score": 960},
    {"word": "cold", "score": 959}, {"word": "calm", "score": 958},
    {"word": "empty", "score": 957}, {"word": "limitless", "score": 956},
    {"word": "restless", "score": 955}, {"word": "south", "score": 954},
    {"word": "trackless", "score": 953}, {"word": "tempestuous", "score": 952},
    {"word": "troubled", "score": 951}, {"word": "universal", "score": 950},
    {"word": "cosmic", "score": 949}, {"word": "turbulent", "score": 948},
    {"word": "adjacent", "score": 947}, {"word": "illimitable", "score": 946},
    {"word": "largest", "score": 945}, {"word": "milky", "score": 944},
    {"word": "huge", "score": 943}, {"word": "angry", "score": 942},
    {"word": "outer", "score": 941}, {"word": "polar", "score": 940},
    {"word": "northeastern", "score": 939}, {"word": "aerial", "score": 938},
    {"word": "primordial", "score": 937}, {"word": "atmosphere", "score": 936},
    {"word": "unfathomable", "score": 935}, {"word": "gray", "score": 934},
    {"word": "fathomless", "score": 933}, {"word": "nearby", "score": 932},
    {"word": "rough", "score": 931}, {"word": "primitive", "score": 930},
    {"word": "deepest", "score": 929}, {"word": "northwestern", "score": 928},
    {"word": "southwest", "score": 927}, {"word": "west", "score": 926},
    {"word": "eternal", "score": 925}, {"word": "boisterous", "score": 924},
    {"word": "stratified", "score": 923}, {"word": "northwest", "score": 922},
    {"word": "pacific", "score": 921}, {"word": "two", "score": 920},
    {"word": "veritable", "score": 919}, {"word": "mysterious", "score": 918}
]

submitted_word = "Galaxy"  

adjectives = []
for item in data:
    adjectives.append(item["word"])

adjective_list = ', '.join(adjectives)
sentence = f"The {submitted_word} is {adjective_list}."

print(sentence)