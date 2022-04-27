#include "lists.h"

/**
  * insert_node - function in C that inserts a
  * number into a sorted singly linked list.
  * @head: head of the node
  * @number: number to be inserted in the list.
  * Return: the address of the new node, or NULL if it failed
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	/*If the node is the first node to the list*/
	if (ptr == NULL || number <= 0)
	{
		node->next = ptr;
		*head = node;
		return (node);
	}
	while (ptr->next != NULL)
	{
		if (ptr->next->n >= number)
		{
			node->next = ptr->next;
			ptr->next = node;
			return (node);
		}
		ptr = ptr->next;
	}
	ptr->next = node;
	node->next = NULL;
	return (node);
}
