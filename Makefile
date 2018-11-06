test:
	#python3 -m unittest
	coverage run -m unittest
		coverage report -m
.PHONY: test
