#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 *print_python_list_info - Prints some basic info about Python list
 *@p: Pointer to a Python object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObjetct *)p)->allocated;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %li: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
