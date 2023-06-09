CMAINFILE   = reverse-linked-list.c
PACKAGE		?= $(shell cd ./go && go list)

default: all

pkgname:
	$(info ${PACKAGE})

py-test:
	@python3 -m unittest discover -v -s python -p '*_test.py'

go-fmt:
	@cd go && \
		go fmt &&\
		cd ..

go-test: go-fmt
	@cd go &&\
		go test -v -timeout 30s ${PACKAGE} &&\
		cd ..

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

all: py-test pkgname go-test c-test