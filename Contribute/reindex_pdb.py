import os
import sys

def next_traj_pdb(trajpdb):
    lines = []
    count = 0
    for line in open(trajpdb):
        if line.startswith("ATOM"):
            count += 1
            line = line[:6] + "%6d" % count + line[12:]
        lines.append(line)
        if line.startswith("ENDMDL"):
            yield "".join(lines)
            count = 0
            lines = []

if __name__ == "__main__":
    input_trajpdb = sys.argv[1]
    os.system(f"{input_trajpdb} {input_trajpdb}.bak.pdb")
    with open(input_trajpdb,"w") as f:
        for pdbblock in next_traj_pdb(f"{input_trajpdb}.bak.pdb"):
            f.write(pdbblock)
    print(f"Transformation done for {input_trajpdb} in place.")
