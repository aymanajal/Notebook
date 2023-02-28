# RAID类型介绍
 
 ## 概念介绍  
RAID (Redundant Array of Independent/InexpensiveDisks)，独立磁盘冗余阵列，是一种将多块独立的硬盘（物理硬盘）按不同的组合方式形成一个硬盘组（逻辑硬盘），从而提供比单块硬盘更大的存储容量、更高的可靠性和 更快的读写性能等。  

---

## RAID级别  

- RAID0： 
   
![v](https://www.dell.com/community/image/serverpage/image-id/44112i4C8058239A94995A/image-size/medium?v=v2&px=400)  

 
RAID0 主要通过将多块硬盘“串联”起来，从而形成一个更大容量的逻辑硬盘。RAID0通过“条带化（striping）”将数据分成不同的 数据块，并依次将这些数据块写到不同的硬盘上。因为数据分布在不同的硬盘上，所以数据吞吐量得到大大提升。但是，很容易看出RAID0没有任何数据冗余， 因此其可靠性不高。  

 - RAID1: 

![v](https://www.dell.com/community/image/serverpage/image-id/44113i37BEDBC735090BA1/image-size/medium?v=v2&px=400)  


  RAID1 被称为磁盘镜像，即所有的数据都会写入至少两块独立的物理磁盘。将每一份数据都同时写到多块硬盘（一般是两块）上去，从而实现了数据的完全备份。假如一块磁盘发生故障，另一块磁盘仍可用于数据应用，因此数据可靠性程度较高；

- RAID2:

![v](https://www.dell.com/community/image/serverpage/image-id/44114iF64FAC08632123E4/image-size/medium?v=v2&px=400)  

AID 2以比特（bit）为单位，将数据―“条带化（striping）”分布存储在不同硬盘上；同时，将不同硬盘上同一位置的数据位用海明码进行编码，并将这些 编码数据保存在另外一些硬盘的相同位置上，从而实现错误检查和恢复。

近年以来，汉明码已被用作用于磁盘驱动器的纠错码，故此RAID 2已不再有使用。

- RAID3:  

![v](https://www.dell.com/community/image/serverpage/image-id/44115i7A6742D3734D80B3/image-size/medium?v=v2&px=400)  

RAID 3所使用的技术被称为奇偶校验磁盘，将RAID控制器生成的奇偶校验信息存储到与实际数据磁盘分开的磁盘上，而非像RAID 5那样和数据在一起条带化。


- RAID4:
  
![v](https://www.dell.com/community/image/serverpage/image-id/44116iAAF24A530D703633/image-size/medium?v=v2&px=400)  

与RAID 3的分布结构类似，不同的是RAID 4以数据块（block）为单位进行奇偶校验码的计算。另外，与RAID2和RAID3不同的是，RAID4中各个磁盘是独立操作的，并不要求各个磁盘的磁头同步转动。

- RAID5：

![v](https://www.dell.com/community/image/serverpage/image-id/44117i33C7D0BD2D4B385D/image-size/medium?v=v2&px=400)  

RAID 5使用磁盘条带化与奇偶校验技术。数据分布在RAID集合的所有磁盘上，并且和在发生磁盘故障，进行数据重构时所用的奇偶校验信息混合在一起。RAID 5至少需要三块物理磁盘。

- RAID6:

![v](https://www.dell.com/community/image/serverpage/image-id/44118i28589C940E79175E/image-size/medium?v=v2&px=400)  

在RAID 5的基础上，RAID 6又另外增加了一组奇偶校验码，从而获得更高的容错性，最多允许同时有两块硬盘出现故障。但是，新增加的奇偶校验计算同时也带来了写操作性能上的损耗。

- RAID 0+1

RAID 0+1: 为了获取更好的I/O吞吐率或者可靠性，将不同的RAID标准级别混合产生的组合方式叫做嵌套式RAID，或者混合RAID。RAID0+1 是先将硬盘分 为若干组，每组以RAID0的方式组成―条带化‖的硬盘阵列，然后将这些组RAID0的硬盘阵列以RAID1的方式组成一个大的硬盘阵列。

- RAID10:
  
![v](https://www.dell.com/community/image/serverpage/image-id/44120i876ABBBF6A1155DB/image-size/medium?v=v2&px=400)  

类似于RAID 0+1， RAID 10则是先“镜像”（RAID 1）、后“条带化”（RAID0）。RAID0+1和RAID10性能上并无太大区别，但是RAID10在可靠性上要好于RAID0+1。这是因为在 RAID10中，任何一块硬盘出现故障不会影响到整个磁盘阵列，即整个系统仍将以RAID10的方式运行；而RAID0+1中，一个硬盘出现故障则会导致 其所在的RAID0子阵列全部无法正常工作，从而影响到整个RAID0+1磁盘阵列 – 在只有两组RAID0子阵列的情况下，整个系统将完全降级为RAID0级别。

