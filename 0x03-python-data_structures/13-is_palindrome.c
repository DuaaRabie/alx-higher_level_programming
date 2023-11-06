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
	listint_t *slow = *head, *fast = *head, *temp;
	listint_t *prev = NULL, *secondhalf, *firsthalf = *head, *sechead;
	int check = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	sechead = slow;
	prev->next = NULL;
	secondhalf = reverse_listint(&sechead);
	temp = secondhalf;
	while (firsthalf && secondhalf)
	{
		if (firsthalf->n != secondhalf->n)
		{
			check = 0;
			break;
		}
		firsthalf = firsthalf->next;
		secondhalf = secondhalf->next;
	}
	secondhalf = reverse_listint(&temp);
	prev->next = secondhalf;
	return (check);
}
