#include <Python.h>

/**
 * print_python_list_info - Print basic info about Python lists.
 *
 * @p: A pyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, index;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < size; index++)
	{
		printf("Element %d", index);

		obj = PyListGetItem(p, index);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
