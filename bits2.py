from qiskit import QuantumProgram
import Qconfig

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set the APIToken and API url

# set up registers and program
qr = qp.create_quantum_register('qr', 2)
cr = qp.create_classical_register('cr', 2)
qc = qp.create_circuit('smiley_writer', [qr], [cr])

# rightmost eight (qu)bits have ')' = 00101001
qc.x(qr[0])
qc.x(qr[1])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[2]) # create superposition on 9
qc.cx(qr[2],qr[2]) # spread it to 8 with a cnot
qc.x(qr[2])

# measure
for j in range(2):
    qc.measure(qr[j], cr[j])

# run and get results
results = qp.execute(["smiley_writer"], backend='ibmqx5', shots=1024)
stats = results.get_counts("smiley_writer")
