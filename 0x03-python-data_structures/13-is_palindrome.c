#include "lists.h"

/**
 * reverse_listint - reverse the list
 * @head: address to the first pointer
 * Return: pointer to the first node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *after = NULL, *prev = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);

	while (current != NULL)
	{
		after = current->next;
		current->next = prev;
		prev = current;
		current = after;
	}
	*head = prev;

	return (*head);
}

/**
 * is_palindrome - check if a singly linked list is palindrome.
 * @head: pointer to the first node
 * Return: 0 if not palindrome || 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list1 = *head, *list2 = NULL, *temp = NULL;
	int length1 = 0, length2 = 0;

	if (*head == NULL)
		return (1);

	while (list1)
	{
		list1 = list1->next;
		length1++;
	}
	list1 = *head;
	if (length1 % 2 != 0)
		length1++;
	while (length2 < length1)
	{
		if (length2 > length1 / 2)
			add_nodeint_end(&list2, list1->n);
		list1 = list1->next;
		length2++;
	}
	list2 = reverse_listint(&list2);
	list1 = *head;
	temp = list2;
	while (temp)
	{
		if (temp->n != list1->n)
			return (0);
		temp = temp->next;
		list1 = list1->next;
	}
	return (1);
}
