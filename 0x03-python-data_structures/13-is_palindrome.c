#include "lists.h"

/**
 * check_palindrome - check_palindrome
 * @head: double pointer
 * @last: pointer
 *
 * Return: 1 or 0
 */
int check_palindrome(listint_t **head, listint_t *last)
{
	if (last->next != NULL)
	{
		if (check_palindrome(head, last->next) == 0)
			return (0);
	}
	if ((*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - is_palindrome
 * @head: double pointer
 *
 * Return: 0, 1
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return (check_palindrome(head, *head));
}
