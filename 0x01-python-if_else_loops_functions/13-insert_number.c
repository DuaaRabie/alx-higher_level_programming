#include "lists.h"
#include <stdio.h>

/**
 * insert_node - insert a new node in a given position
 * @head: address of the first pointer
 * @number: number to be inseted
 * Return: address of new node | NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new;
	int val;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	val = temp->n;

	if (temp == NULL || val > number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next->n < number && temp->next != NULL)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;

	return (new);
}
