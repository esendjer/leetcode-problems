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

all: py-test pkgname go-test