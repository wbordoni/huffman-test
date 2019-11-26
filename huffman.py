import sys
import time
import heapq

class Huffman:

    def __init__(self):
        self.occ = {}
        self.sorted_occ = {}
        self.start_time = time.time()
        self.tree = None

    def print_message(self, msg):
        t = time.time() - self.start_time 
        print("[{:06.4f}] {} ".format(t, msg))


    def build_huffman_tree(self):
        """
        Build the huffman tree
        
        self.tree = [(f, {'v':k}) for (k, f) in self.sorted_occ.items()]
        #heapq.heapify(self.tree)

        while len(self.tree) < 2:
            f1, left = heapq.heappop(self.tree)
            f2, right = heapq.heappop(self.tree)
            heapq.heappop(self.tree, (f1 + f2, {'left': left, 'right': right}))

        self.print_message("Huffman tree built (length={}).".format(len(self.tree)))
        _, ret = heapq.heappop(self.tree)
        return ret
        """
        return None
	    


    def build_occurency_table(self, filename):
        """
        Build the occurency table of characters in filename

        Args:
            filename: the name of the file to parse
        """
        with open(filename) as fn:
            ln = fn.readline()
            while ln:
                for i in ln.strip():
                    if i in self.occ:
                        self.occ[i]+=1
                    else:
                        self.occ[i]=1
                ln = fn.readline()
        
        self.print_message("Occurency table built (length={})".format(len(self.occ)))

    def sort_occurency_table(self):
        """
        Sort occurency table by descending order 
        """
        self.sorted_occ = {k: v for k, v in sorted(self.occ.items(), key=lambda x: x[1])}
        self.print_message("Occurency table sorted.")

    def print_occurency_table(self):
        self.print_message(self.sorted_occ)


def main(filename):
    hf = Huffman()
    hf.print_message("Starting Huffman algorithm ({}) :".format(filename))
    hf.build_occurency_table(filename)
    hf.sort_occurency_table()
    #hf.print_occurency_table()
    hf.build_huffman_tree()

    hf.print_message("Huffman algorithm done.")


if __name__ == '__main__':
        main(sys.argv[0])
