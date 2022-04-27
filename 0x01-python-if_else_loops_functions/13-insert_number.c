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
	listint_t *node = *head;
	listint_t *new_node = NULL;

	/* crear el nodo */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if (node->n > number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	/* validar la posicion donde ubicarlo */
	while (node->next != NULL)
	{
		/* si encuentra la posicion */
		if (node->next->n > number)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}
