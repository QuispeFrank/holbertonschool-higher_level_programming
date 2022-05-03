#include "lists.h"

/**
 * listint_len - function that returns the
 * number of elements in a linked list_t list
 * @h: head of the linked list
 * Return: a function that returns the number
 * of elements in a linked listint_t list.
 */

size_t listint_len(const listint_t *h)
{
	size_t counter = 0;

	for (; h; counter++)
	h = h->next;

	return (counter);
}

/**
 * node_at_index -  a function that returns the nth
 * node of a listint_t linked list.
 *
 * @head: a pointer to the head of the single
 * linked list.
 * @index: the index of the node.
 * Return: @n data.
 */

listint_t *node_at_index(listint_t *head, unsigned int index)
{
	listint_t *node = NULL;

	/* validacion de nodos nulos */
	if (!head)
		return (NULL);
	/* si solo existe un nodo */
	if (!index)
		return (head);

	node = head;
	/* si existen mas nodos */
	while (index--)
	{
		if (!node)
			break;
		node = node->next;
	}
	return (node);
}
/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome.
 * @head: head of the single linked list.
 *
 * Return: 1 if it's palindrome, 0 else.
 */
int is_palindrome(listint_t **head)
{
	listint_t *left_node = NULL;
	listint_t *right_node = NULL;
	int list_len, i = 0, j;
	int palindrome = 0;

	/* un solo elemento es palindrome */
	if (*head == NULL)
		return (0);

	list_len = listint_len(*head);
	if (list_len == 0)
		return (0);
	if (list_len == 1)
		return (1);

	j = list_len - 1;
	for (i = 0; i < list_len / 2; i++, j--)
	{
		left_node = node_at_index(*head, i);
		right_node = node_at_index(*head, j);

		if (left_node->n == right_node->n)
		{
			palindrome = 1;
			continue;
		}
		palindrome = 0;
	}
	return (palindrome);
}
