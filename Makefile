donut: clean
	$(CC) -Wunused-function -Wall -fpack-struct=8 -DDONUT_EXE -I include donut.c hash.c encrypt.c format.c loader/clib.c -odonut
	$(CC) -Wunused-function -Wall -c -fpack-struct=8 -fPIC -I include donut.c hash.c encrypt.c format.c loader/clib.c
	$(AR) rcs lib/libdonut.a donut.o hash.o encrypt.o format.o clib.o
	$(CC) -Wall -shared -o lib/libdonut.so donut.o hash.o encrypt.o format.o clib.o
debug: clean
	$(CC) -Wunused-function -ggdb -Wall -Wno-format -fpack-struct=8 -DDEBUG -DDONUT_EXE -I include donut.c hash.c encrypt.c format.c loader/clib.c -odonut
hash:
	$(CC) -Wall -Wno-format -fpack-struct=8 -DTEST -I include hash.c loader/clib.c -ohash
encrypt:
	$(CC) -Wall -Wno-format -fpack-struct=8 -DTEST -I include encrypt.c loader/clib.c -oencrypt
inject:
	$(CC) -Wall -Wno-format -fpack-struct=8 -DTEST -I include loader/inject.c -oinject
inject_local:
	$(CC) -Wall -Wno-format -fpack-struct=8 -DTEST -I include loader/inject_local.c -oinject_local
clean:
	$(RM) loader.exe exe2h.exe exe2h loader32.exe loader64.exe donut.o hash.o encrypt.o format.o clib.o hash encrypt donut hash.exe encrypt.exe donut.exe lib/libdonut.a lib/libdonut.so
