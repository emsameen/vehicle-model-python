# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

# pylint: disable=C0103

from sdv.model import Service
from sdv_model.proto.trunk_pb2 import (
  SetLockStateRequest,
  OpenRequest,
  CloseRequest,
  TrunkInstance,
  LockState
)
from sdv_model.proto.trunk_pb2_grpc import TrunkStub


class TrunkService(Service):

    def __init__(self):
        super().__init__()
        self._stub = TrunkStub(self.channel)

    async def SetLockStateRequest(self, instance: TrunkInstance, state: LockState):
        response = await self._stub.SetLockStateRequest(SetLockStateRequest(instance=instance, state=state), metadata=self.metadata)
        return response

    async def Open(self, instance: TrunkInstance):
        response = await self._stub.Open(
            OpenRequest(instance=instance),
            metadata=self.metadata,
        )
        return response

    async def Close(self, instance: TrunkInstance):
        response = await self._stub.Close(
            CloseRequest(instance=instance),
            metadata=self.metadata,
        )
        return response
