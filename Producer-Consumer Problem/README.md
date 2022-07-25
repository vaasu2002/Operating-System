# Producer-Consumer Problem
#### **AIM:**
To Write a C program to simulate producer-consumer problem using semaphores. 
#### **DESCRIPTION:** 
Producer consumer problem is a synchronization problem. There is a fixed size buffer where the producer produces items and that is consumed by a consumer process. One
solution to the producer consumer problem uses shared memory. To allow producer and consumer processes to run concurrently, there must be available a buffer of items 
that can be filled by the producer and emptied by the consumer. This buffer will reside in a region of memory that is shared by the producer and consumer processes. 
The producer and consumer must be synchronized, so that the consumer does not try to consume an item that has not yet been produced.  
