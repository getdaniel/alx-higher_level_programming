#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 *
 * @p: A PyObject list object.
 *
 * Return: Void.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, index;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");

		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (index = 0; index < size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[index]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 *
 * @p: A PyObject byte object.
 *
 * Return: Void.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, index;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");

		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (index = 0; index < size; index++)
	{
		printf("%02hhx", bytes->ob_sval[index]);
		if (index == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 *
 * @p: A PyObject float object.
 *
 * Return: Void.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
