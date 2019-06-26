# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  add_two_numbers_with_carry(l1,l2)
end

# @param {ListNode} l1
# @param {ListNode} l2
# @param {Integer} c
# @return {ListNode}
def add_two_numbers_with_carry(l1, l2, c: 0)
  if l1.nil? and l2.nil?
    if c == 0
      return nil
    else
      return ListNode.new(c)
    end
  end
  if l1.nil?
    curr_sum, curr_carry = add_two_num_w_carry({x: 0, y: l2.val,c: c})
    return create_return_node(sum: curr_sum, carry: curr_carry) if l2.next.nil?
    l1 = ListNode.new(0)
  elsif l2.nil?
    curr_sum, curr_carry = add_two_num_w_carry({x: l1.val,y: 0,c: c})
    return create_return_node(sum: curr_sum, carry: curr_carry) if l1.next.nil?
    l2 = ListNode.new(0)
  else
    curr_sum, curr_carry = add_two_num_w_carry({x: l1.val,y: l2.val,c: c})
  end
  sum = ListNode.new(curr_sum)  
  sum.next = add_two_numbers_with_carry(l1.next,l2.next,c: curr_carry)
  sum
end

# @param {Integer} x
# @param {Integer} y
# @param {Integer} c
# @return [Integer, Integer] sum, carry
def add_two_num_w_carry(x: 0,y: 0,c: 0)
  sum = x+y+c
  carry = (sum / 10).to_i
  sum %= 10
  [sum,carry]
end

# @param {Integer} sum
# @param {Integer} carry
# @return {ListNode}
def create_return_node(sum: 0, carry: 0)
  if carry != 0
    carry_node = ListNode.new(carry)
    s_node = ListNode.new(sum)
    s_node.next = carry_node
    return s_node
  else
    ListNode.new(sum)
  end
end
