#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *current;

	current = *head;
	while(current->next && current->next->next)
	{
		slow = current->next;
		fast = current->next->next;
		if (slow == fast)
		{
			return (1);
		}
		else
		{
			return (0);
		}

	}
	return (0);
}

