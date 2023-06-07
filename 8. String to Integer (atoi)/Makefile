CMAINFILE=string_to_integer_atoi.c

default: all

py-test:
	@python3 -m unittest discover -v -s python -p '*_test.py'

c-build:
	@cd c &&\
		gcc ./$(CMAINFILE) && \
		chmod +x a.out && \
		./a.out && \
		cd ..

c-clean:
	@cd c &&\
		$(RM) -f a.out && \
		cd ..

c-test: c-build c-clean

all: py-test c-test