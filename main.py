# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import random
import networkx as nx


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dir = "E:\\wen\Downloads\\Telegram Desktop\\"
    file_list = os.listdir(dir)
    for f in file_list:
        #print(f)
        print("_".join(f[0:-4])+f[-4:])
        os.rename(dir+f, dir+"_".join(f[0:-4])+f[-4:])
        #os.rename(dir+f, dir+f.replace('_',''))
        #os.rename(dir + f, dir+f+".mp")
    '''
    #z = [2,3,4,5]
    #print(z)
    #G = nx.random_degree_sequence_graph(z)

    #print(nx.degree_histogram(G))

    g = nx.dense_gnm_random_graph(1000000, 10000000);
    degree = {}
    for v in g:
        d = len(g[v])
        if len(g[v]) not in degree:
            degree[d] = 0
        degree[d] = degree[d]+1
    outfile = open("direct2.graph", 'w')
    i = 0;
    for e in list(g.edges):
        #print(e[0])
        i = i+1
        if(i%100 == 0):
            print("Current written lines: ", i)
        outfile.write(str(e[0])+"       "+str(e[1]) + "\n")
        outfile.write(str(e[1]) + "       " + str(e[0]) + "\n")
    #for v in g:
    '''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
