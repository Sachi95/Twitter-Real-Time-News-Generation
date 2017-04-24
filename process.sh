cd FOLDER
rm * -rf
cd ..

cd TIME
rm * -rf
cd ..

cd CLEANED_FOLDER
rm * -rf
cd ..

cd FINAL_FOLDER
rm * -rf
cd ..

cd LDA_FOLDER
rm * -rf
cd ..

cd TOPICS
rm * -rf
cd ..

cd NEW_FOLDER
rm * -rf
cd ..

cd DUP_REMOVE_FOLDER
rm * -rf
cd ..

cd SUMMY_FOLDER
rm * -rf
cd ..

echo "Collecting Trending Hashtags from twitter\n"
python3 TrendingHashtags.py > hashtags.txt
cat hashtags.txt
echo ""
echo "Finished Collecting Trending Hashtags\n"

echo "Collecting for each Trending Hashtag top tweets\n"

python3 crawl.py hashtags.txt

python3 init_clean.py

python3 clean.py

echo "Performing Topic Modeling \n"
python3 Topic.py
echo "Finished Topic Modeling \n"

python3 final_topic.py

python3 remove_duplicate.py 

echo "Performing Summarization \n"
python3 temp.py
echo "Finished Summarization \n"
