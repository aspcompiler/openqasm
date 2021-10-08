import logging

from lark import (
        Lark,
        Transformer,
        v_args,
        logger)

from openqasm.ast import (
        AliasStatement,
        AngleType,
        BinaryExpression,
        BitType,
        BoolType,
        BooleanLiteral,
        Box,
        BranchingStatement,
        BreakStatement,
        CalibrationDefinition,
        CalibrationGrammarDeclaration,
        Cast,
        ClassicalArgument,
        ClassicalAssignment,
        ClassicalDeclaration,
        ClassicalType,
        ComplexType,
        Concatenation,
        Constant,
        ConstantDeclaration,
        ConstantName,
        ContinueStatement,
        ControlDirectiveStatement,
        DelayInstruction,
        DurationLiteral,
        DurationOf,
        DurationType,
        EndStatement,
        Expression,
        ExpressionStatement,
        ExternDeclaration,
        FloatType,
        ForInLoop,
        FunctionCall,
        GateModifierName,
        IODeclaration,
        IOKeyword,
        Identifier,
        Include,
        IndexExpression,
        IndexIdentifier,
        IntType,
        IntegerLiteral,
        OpenNode,
        Program,
        QuantumArgument,
        QuantumBarrier,
        QuantumForInLoop,
        QuantumGate,
        QuantumGateDefinition,
        QuantumGateModifier,
        QuantumInstruction,
        QuantumMeasurement,
        QuantumMeasurementAssignment,
        QuantumPhase,
        QuantumReset,
        QuantumStatement,
        QuantumWhileLoop,
        Qubit,
        QubitDeclaration,
        RangeDefinition,
        RealLiteral,
        ReturnStatement,
        Selection,
        Slice,
        Span,
        Statement,
        StretchType,
        StringLiteral,
        SubroutineDefinition,
        Subscript,
        TimeUnit,
        TimingStatement,
        UintType,
        UnaryExpression,
        WhileLoop
    ) 

logger.setLevel(logging.DEBUG)

class QASMASTGenerator(Transformer):
    """
    Class for generating OpenQASM3 reference Python AST.
    """
    
    @v_args(inline=True)
    def program(self, header, global_statement, statement):
        print(type(header), header.data)
        print(type(global_statement))
        print(type(statement))
    
with open("qasm3.lark", "r") as grammar_file:
    qasm_grammar = grammar_file.read()

qasm_parser = Lark(qasm_grammar,
                   parser='lalr',
                   start="program",
                   propagate_positions=False,
                   maybe_placeholders=False,
                   regex=True,
                   debug=True,
                   transformer=QASMASTGenerator())

import os
test_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(test_dir))))  # project root dir
examples_path = os.path.join(root_dir, "examples/")

with open(os.path.join(examples_path, "rb.qasm")) as test_file:
    source = test_file.read()

qasm_parser.parse(source)
