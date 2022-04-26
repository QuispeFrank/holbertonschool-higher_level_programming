#include "lists.h"

/**
  * check_cycle - checks if a singly linked list
  * has a cycle in it.
  * @list: is a pointer to head of the Node
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *double_p = list;
	listint_t *single_p = list;

	/* Validate if find a cycle list */
	while (single_p != NULL)
	{
		/* se mueven los nodos */
		if (double_p->next == NULL || double_p->next->next == NULL)
			return (0);
		double_p = double_p->next->next;
		single_p = single_p->next;
		if (double_p == single_p)
			return (1);
	}
	return (0);
}
