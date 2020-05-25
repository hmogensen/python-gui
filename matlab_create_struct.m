b_struct = struct('a', 'A');
c_struct = struct('aa', b_struct, 'bb', 2);
s = struct('a', 1, 'bb', c_struct, 'b', b_struct, 'c', 2:-1:-4, 'd', 2.1:.1:4, 'FG', 'abcs');
save('example.mat', 's', 'b_struct')

