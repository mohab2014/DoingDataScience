# DoingDataScience: Hash-based Similarity Detection

## Introduction
Motivation
Goal: find similar columns/tables

## Related Work

Hashing - an approach transforming the data item to a low-dimensional representation, or equivalently a short code consisting of a sequence of bits [2]. “Most hash functions are used to separate and obscure data, so that similar data hashes to very different keys.” [3]

Locality-sensitive hashing (LSH) - a simple and powerful technique, which places similar documents with identical hash into the same bucket, performing probabilistic dimension reduction of high-dimensional data and solving the approximate or exact Near Neighbor Search. [Indyk and Motwani, 1998] [4,8]
Nilsimsa [9] - an LSH algorithm for text similarity comparisons, which is traditionally employed for spam detection in emails. Unlike hashes, a small change in the message results in a small change in the nilsimsa code.

SimHash [3,5-7] - an easy and very fast algorithm used to compare two datasets (e.g. texts).

Distance measures:
Hamming distance measures the proportion of positions in the hash at which the corresponding symbols are different.

## Method
Hash-based Similarity Detection Algorithm:
Read csv tables from the dataset
Find similar columns:
Compute hash for each column (hash features) ?
Compute hash similarities (compare columns)
Find similar tables:
Compute hash for each table (hash features, e.g. columns or their hashes)
Compute table similarities (compare tables)

## References
[1] Das Sarma, Anish, et al. "Finding related tables." Proceedings of the 2012 ACM SIGMOD International Conference on Management of Data. ACM, 2012.
http://i.stanford.edu/~anishds/publications/sigmod12/modi255i-dassarma.pdf

[2] Hashing for Similarity Search: A Survey.
http://arxiv.org/pdf/1408.2927.pdf

[3] SimHash: Hash-based Similarity Detection.
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.473.7179&rep=rep1&type=pdf

[4] Similarity search in high dimensions via hashing.
https://www.cs.princeton.edu/courses/archive/spring13/cos598C/Gionis.pdf

[5] http://matpalm.com/resemblance/simhash/

[6] Similarity Estimation Techniques from Rounding Algorithms.
http://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarEstim.pdf

[7] A Python Implementation of Simhash Algorithm.
https://github.com/leonsim/simhash

[8] LSH Algorithm and Implementation (E2LSH).
http://www.mit.edu/~andoni/LSH/

[9] https://github.com/diffeo/py-nilsimsa/
