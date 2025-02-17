all: clean data_cleaning data_merging analysis correlation model

clean:
	rm -f data/2018_cleaned.csv
	rm -f data/happiness_combined.csv

data_cleaning:
	python src/data_cleaning.py

data_merging:
	python src/data_merging.py

analysis:
	python src/exploratory_analysis.py

correlation:
	python src/correlation_analysis.py

model:
	python src/regression_model.py
