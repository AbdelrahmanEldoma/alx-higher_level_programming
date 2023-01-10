#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	size = PyList_Size(p);
	printf("%d", size);
}