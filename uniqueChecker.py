def check():
    lines_seen = set()  # holds lines already seen
    outfile = open("paginalijst-uniques.txt", "w")
    for line in open("paginalijst-combined.txt", "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()


if __name__ == "__main__":
    check()
