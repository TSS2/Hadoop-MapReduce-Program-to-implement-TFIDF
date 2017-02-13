1. I've added the output files which I got from running the below commands.
2. All the mappers and reducers are present in a filder named hadoop_docs. Please copy this folder in order to run the below commands as is also included in the hadoop_docs folder.
3. Run the below commands:

rm -rf output
$HADOOP/bin/hadoop jar $HADOOP/contrib/streaming/hadoop-streaming-1.2.1.jar -input hadoop_docs/input -output output -mapper hadoop_docs/mapper.py -reducer hadoop_docs/reducer.py
cp output/part-00000 reducer_output1.txt

rm -rf output
$HADOOP/bin/hadoop jar $HADOOP/contrib/streaming/hadoop-streaming-1.2.1.jar -input reducer_output1.txt -output output -mapper hadoop_docs/mapper2.py -reducer hadoop_docs/reducer2.py
cp output/part-00000 reducer_output2.txt

rm -rf output
$HADOOP/bin/hadoop jar $HADOOP/contrib/streaming/hadoop-streaming-1.2.1.jar -input reducer_output2.txt -output output -mapper hadoop_docs/mapper3.py -reducer hadoop_docs/reducer3.py
cp output/part-00000 reducer_output3.txt

rm -rf output
$HADOOP/bin/hadoop jar $HADOOP/contrib/streaming/hadoop-streaming-1.2.1.jar -D mapred.reduce.tasks=0 -input reducer_output3.txt -output output -mapper hadoop_docs/mapper4.py
cp output/part-00000 mapper_output4.txt